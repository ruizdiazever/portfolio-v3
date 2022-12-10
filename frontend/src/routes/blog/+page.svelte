<script>
	import axios from "axios";
    import Loader from "$lib/components/Loader.svelte";

	let blog = [];
    let path = import.meta.env.VITE_API_ENPOINT
    let showLoader = true

    const graphqlQuery = {
        "operationName": "Blog",
        "query": `query Blog { blog { title, date } }`,
        "variables": {}
    };

    async function getBlog() {
        let headers = { headers: { "Content-Type": "application/json" } };
        try {
            await axios.post(path, graphqlQuery, headers).then((response) => {
                blog = response.data.data.blog;
                showLoader = false;
            });
        } catch (error) {
            console.log(error.message);
        }
    }
    getBlog();
</script>

<svelte:head>
	<title>Blog</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="main-page">
	<h1>Blog</h1>
	<p class="subtitle-page">You can see here my contributions, blog and more</p>
	<div class="mb-5 mt-10">
		{#if showLoader}
			<Loader />
		{:else}
			<ul>
				{#each blog as item}
				<li class="blog-li"><code class="blog-li-span text-sm">{item.date}</code><span class="ml-5 blog-li-span-2">{item.title}</span></li>
				{/each}
			</ul>
		{/if}
	</div>
</div>
