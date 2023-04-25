from twarc import Twarc2, expansions
import json

client = Twarc2(bearer_token="CXXCXXCXX")

def main():
    
    existing_rules = client.get_stream_rules()
    if 'data' in existing_rules and len(existing_rules['data']) > 0:
        rule_ids = [rule['id'] for rule in existing_rules['data']]
        client.delete_stream_rule_ids(rule_ids)

    
    new_rules = [
        {"value": "covid OR covid19 lang:en", "tag": "covid-related-tweets"},
        {"value": "corona OR coronavirus", "tag": "corona-related-tweets"}
    ]
    added_rules = client.add_stream_rules(rules=new_rules)


    for count, result in enumerate(client.stream()):
       
       
        tweet = expansions.flatten(result)

        print(json.dumps(tweet))
       
        if count > 100:
            break

   
    rule_ids = [rule['id'] for rule in added_rules['data']]
    client.delete_stream_rule_ids(rule_ids)

if __name__ == "__main__":
    main()
