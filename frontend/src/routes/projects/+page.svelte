<script>
	import axios from "axios";
	import Loader from "$lib/components/Loader.svelte";
	import berli_cover from "$lib/images/berli.jpg";
	import blog_cover from "$lib/images/blog.jpg";
	import bot_cover from "$lib/images/bot.jpg";
	import ecommerce_cover from "$lib/images/ecommerce.jpg";
	import portfoliov3 from "$lib/images/portfolio_v3.jpg";
	import portfoliov4 from "$lib/images/portfolio_v4.jpg";

	let projects = [];
    let path = import.meta.env.VITE_API_ENPOINT
    let showLoader = true
	let covers = {
		"berli_cover": berli_cover, 
		"blog_cover": blog_cover, 
		"bot_cover": bot_cover, 
		"ecommerce_cover": ecommerce_cover,
		"portfoliov3_cover": portfoliov3,
		"portfoliov4_cover": portfoliov4
	}

    const graphqlQuery = {
        "operationName": "Project",
        "query": `query Project { project { title, subtitle, url, cover, stack, position } }`,
        "variables": {}
    };

    async function getProjects() {
        let headers = { headers: { "Content-Type": "application/json" } };
        try {
            await axios.post(path, graphqlQuery, headers).then((response) => {
                projects = response.data.data.project;
				projects.sort(compareResults);
                showLoader = false;
            });
        } catch (error) {
            console.log(error.message);
        }
    }

	function compareResults(a, b) {
		if (a.position < b.position) {
			return 1;
		}
		if (a.position > b.position) {
			return -1;
		}
		return 0;
	}

    getProjects();
</script>

<svelte:head>
	<title>Projects</title>
	<meta name="description" content="Some of my projects" />
</svelte:head>

<main class="main-page">
	<h1>Projects</h1>
	<p class="subtitle-page">Some of my project, you can see more in my GitHub</p>


	<!-- CARD -->
	<div class="project-container">
		{#if showLoader}
			<Loader />
		{:else}
			{#each projects as project}
				<div class="card">
					<div class="card-header">
						<img src={covers[project.cover]} class="card-img rounded-[24px]" alt="Logo">
					</div>
					<div class="card-body py-6">
						<a href="{project.url}" target="blank">
							<h2 class="text-xl text-center dark:text-green-300">{project.title}</h2>
						</a>
						<p class="mt-2 text-center">{project.subtitle}</p>
						<p class="stack text-center mx-auto mt-3"><small class="dark:text-gray-400">{project.stack}</small></p>
					</div>
				</div>
			{/each}
		{/if}
	</div>
</main>

<style>
	.card-img {
		width: 290px;
		height: 120px;
		object-fit: cover;
	}

	.stack {
		max-width: 260px;
	}

	.project-container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }
</style>