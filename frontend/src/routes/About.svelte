<script>
    import axios from "axios";
    import Header from "./sections/Header.svelte"

    let name = "404";
    async function getData() {
        const path = "http://127.0.0.1:8000/api/v1/about";
        let headers = { headers: { "Content-Type": "application/json" } };
        await axios.get(path, headers).then((response) => {
            name = response.data.name;
        });
    }
    getData();
</script>

<main>
    <Header />

    <div class="mt-6">
        <p class="text-2xl">{@html name}</p>
    </div>
</main>

<style>
</style>