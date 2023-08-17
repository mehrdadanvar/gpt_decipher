import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
  organization: process.env.ORGANIZATION,
  apiKey: process.env.OPENAI_API_KEY,
});
// console.log(configuration);
const openai = new OpenAIApi(configuration);
export default defineEventHandler(async (event) => {
  let run_query = async () => {
    try {
      console.log(configuration);
      // let sample = await openai.listModels();
      // console.log(sample.data.data);
      let completion = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [
          {
            role: "user",
            content:
              "provide a JSON object describing a patients history,presentation, physical exam and lab findings with acute pancreatitis. do not include any other text or newline characters so that the json object could be parsed easily. ",
          },
        ],
        max_tokens: 2048,
      });
      let answer: any = completion.data.choices[0];
      console.log(answer["message"]["content"]);
      let gpt_response = answer["message"]["content"];
      return JSON.parse(gpt_response);
    } catch (error) {
      error ? console.log(error) : "";
    }
  };
  let data = await run_query();
  return { response: data };
});
