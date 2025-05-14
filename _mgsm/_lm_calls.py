import openai
import backoff
import json

client = openai.OpenAI()

COST_PER_TOKEN = {
    "gpt-3.5-turbo-0125": {"input": 0.50 / 1000000 , "output": 1.50 / 1000000 },
    "gpt-4-turbo-2024-04-09": {"input": 10.00 / 1000000, "output": 30.00 / 1000000},
    "gpt-4o-2024-05-13": {"input": 5.00 / 1000000, "output": 15.00 / 1000000},
}

def compute_cost(model, input_usage, output_usage):
    input_price, output_price = COST_PER_TOKEN[model]["input"], COST_PER_TOKEN[model]["output"]
    input_cost = input_usage * input_price
    output_cost = output_usage * output_price
    total_cost = input_cost + output_cost
    return total_cost

@backoff.on_exception(backoff.expo, openai.RateLimitError)
def get_json_response_from_gpt(
        msg,
        model,
        system_message,
        temperature=0.5
):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": msg},
        ],
        temperature=temperature, max_tokens=4096, stop=None, response_format={"type": "json_object"}
    )
    content = response.choices[0].message.content
    json_dict = json.loads(content)
    cost = compute_cost(model=model, input_usage=response.usage.prompt_tokens,output_usage=response.usage.completion_tokens )
    assert not json_dict is None
    return json_dict, cost


@backoff.on_exception(backoff.expo, openai.RateLimitError)
def get_json_response_from_gpt_reflect(
        msg_list,
        model,
        temperature=0.8
):
    response = client.chat.completions.create(
        model=model,
        messages=msg_list,
        temperature=temperature, max_tokens=4096, stop=None, response_format={"type": "json_object"}
    )
    content = response.choices[0].message.content
    json_dict = json.loads(content)
    cost = compute_cost(model=model, input_usage=response.usage.prompt_tokens,output_usage=response.usage.completion_tokens)
    assert not json_dict is None
    return json_dict, cost