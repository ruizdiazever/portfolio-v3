<script>
  import { Router, Link, Route } from "svelte-routing";
  import Home from "./routes/Home.svelte";
  import About from "./routes/About.svelte";
  import Blog from "./routes/Blog.svelte";
  import Demo from "./routes/Demo.svelte";
  export let url = "";
</script>

<Router {url}>
      <Route path="blog" component={Blog} />
      <Route path="demo" component={Demo} />
      <Route path="about" component={About} />
      <Route path="/"><Home /></Route>
</Router>