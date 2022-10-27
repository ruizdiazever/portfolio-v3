<script>
    import axios from "axios";
    import Header from "./sections/Header.svelte"

    let name = "404";

    async function getData() {
        const path = "http://127.0.0.1:8000/about";
        let headers = { headers: { "Content-Type": "application/json" } };
        await axios.get(path, headers).then((response) => {
            name = response.data.name;
        });
    }
</script>

<main>
    <Header />
</main>

<style>

</style>
