<script lang="typescript">
        import Chat from "./Chat.svelte";
        import { Router, Route } from "svelte-routing";
	export let url: string = "";
</script>

<Router url="{url}">
    <Route path="chat" component="{Chat}" />
</Router>


<style>
    :global(body){
        margin: 0;
        padding: 0;
    }

</style>
