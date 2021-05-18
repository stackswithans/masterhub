<script lang="typescript">
        import CallHome from "./CallHome.svelte";
        import Call from "./Call.svelte";
        import { Router, Route } from "svelte-routing";
	export let url: string = "";
</script>

<Router url="{url}">
    <Route path="" component="{CallHome}" />
    <Route path="call" component="{CallHome}" />
    <Route path="call/:callId" component="{Call}" />
</Router>


<style>
    :global(body){
        margin: 0;
        padding: 0;
    }

</style>
