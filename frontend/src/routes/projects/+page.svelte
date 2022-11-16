<script>
	import axios from "axios";
	import Loader from "$lib/components/Loader.svelte";
    import pawel from "$lib/images/pawel.jpg";
	import renato from "$lib/images/renato.jpg";
	import czerwinski from "$lib/images/czerwinski.jpg";
	import ramos from "$lib/images/ramos.jpg";

	let projects = [];
    let path = import.meta.env.VITE_API_ENPOINT
    let showLoader = true
	let covers = {
		"pawel": pawel, 
		"renato": renato, 
		"czerwinski": czerwinski, 
		"ramos": ramos
	}

    const graphqlQuery = {
        "operationName": "Project",
        "query": `query Project { project { title, subtitle, url, cover, stack, image } }`,
        "variables": {}
    };

    async function getProjects() {
        let headers = { headers: { "Content-Type": "application/json" } };
        try {
            await axios.post(path, graphqlQuery, headers).then((response) => {
                projects = response.data.data.project;
                showLoader = false;
            });
        } catch (error) {
            console.log(error.message);
        }
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
						<img src={covers[project.image]} class="card-img w-full rounded-[24px]" alt="Logo">
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
        height: 120px;
		width: 290px;
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