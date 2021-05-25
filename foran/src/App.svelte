<script lang="typescript">
        import Landing from "./routes/Landing.svelte";
        import SignUp from "./routes/SignUp.svelte";
        import { Router, Route } from "svelte-routing";
	export let url: string = "";
</script>

<!-- Add fonts -->
<svelte:head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Condensed">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
</svelte:head>

<Router url="{url}">
    <Route path="" component="{Landing}"/>
    <Route path="/register" component="{SignUp}"/>
</Router>

<style>
    :global(html, body, *){
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Roboto", sans-serif;
        height: fit-content;
    }

    :global(body){
        height: fit-content;
    }

    /*color pallete*/
    :global(:root){
        --color-1: #FFC800;
        --color-2: #FFC800;
        --color-3: #404040;
        --color-4: #FAFAFA;
        --color-5: #FFC800;
        --color-6: #969696;
        --color-7: #FFFFFF;
        --color-8: #F0F0EB;
        --color-9: #646464;
        --color-10: #FFC800;
        --color-11: #E4E4E4;
    }
</style>
