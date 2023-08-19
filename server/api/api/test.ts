export default defineEventHandler(async (event) => {
  async function wait() {
    // function timer2(ms:number){
    //   let x :any = new Promise((res)=>{
    //     setTimeout(res,ms)
    //   })

    // }
    const timer = (ms: number) => new Promise((res) => setTimeout(res, ms));
    await timer(20000);
    return 1;
  }
  let data = await wait();
  console.log(data);
  return { response: data };
});
