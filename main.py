import clio

def main():
    # neuron annotations query
    query = '{"bodyid":[154109,24053]}'
    status_code, content = clio.post('prod', 'json-annotations/VNC/neurons/query', str_payload = query)
    if status_code != 200:
        print(f"Error in query request: {status_code}: {content}")
    else:
        print(f"Query result: {content}")

    # point annotation upload
    payload = f'{{"kind": "point", "pos": [13914,12000,8991], "tags": ["Root"], "user": "{clio.user_email}", "description": "This is my point"}}'
    status_code, content = clio.post('test', 'annotations/VNC', str_payload = payload)
    if status_code != 200:
        print(f"Error in point annotation post request: {status_code}: {content}")
    else:
        print(f"Point annotation post result: {content}")


if __name__ == '__main__':
    main()