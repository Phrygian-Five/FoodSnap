import base64
import requests

def vision(imagepath):
  # OpenAI API Key
  file = open("key.txt","r")
  api_key = file.read()
  file.close()

  # Function to encode the image
  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')

  # Path to your image
  image_path = imagepath

  # Getting the base64 string
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Please make a text file-based table of individual ingredients that are in the food that is provided with no further information added, if it is not food, send back an error,thank you!"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 3000
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  print(response.json())
  return(response.json())


def main():
  vision()

if __name__ == "__main__":
  main()