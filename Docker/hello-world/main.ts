import { Application } from "https://deno.land/x/oak/mod.ts";

const app = new Application();

app.use((ctx) => {
  ctx.response.body = "Helloworld from Deno";
});

await app.listen({ port: 8000 });