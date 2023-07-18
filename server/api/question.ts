import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
  organization: process.env.ORGANIZATION,
  apiKey: process.env.OPEN_API_KEY,
});
// console.log(configuration);
const openai = new OpenAIApi(configuration);
export default defineEventHandler(async (event) => {
  let run_query = async () => {
    try {
      // let sample = await openai.listModels();
      // console.log(sample.data.data);
      let completion = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [
          {
            role: "user",
            content:
              "provide a JSON objects describing a patients histroy,presentation, physical exam and labfindings with acute appendicities",
          },
        ],
        max_tokens: 2048,
      });
      console.log(completion.data.choices[0]);
    } catch (error) {
      error ? console.log(error) : "";
    }
  };
  run_query();

  return {
    hello: "world",
  };
});
