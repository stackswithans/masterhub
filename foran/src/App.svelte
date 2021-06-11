<script lang="typescript">
        import Router from "svelte-spa-router";
        import routes from "./routes.js";
</script>

<!-- Add fonts -->
<svelte:head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Condensed">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
    <script src="https://kit.fontawesome.com/4b291d6efe.js" crossorigin="anonymous"></script>
</svelte:head>

<Router {routes} />

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

    :global(.container){
        margin: 0;
        padding: 0;
        box-sizing: border-box;
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
