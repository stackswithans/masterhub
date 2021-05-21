<script lang="typescript">
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

<!-- 
<Router url="{url}">
    <Route path="" component="{}" />
</Router>
 -->

<style>
    :global(body){
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    :global(:root){
        --p-color: #36413E;
        --s-color: #4a5955;
    }
</style>
