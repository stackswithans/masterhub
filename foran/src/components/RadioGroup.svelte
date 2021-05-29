
<script lang="typescript">
    import RegisterRadio from "../components/RegisterRadio.svelte";
    export let options: Array<[string, string]>;
    export let group: string;
</script>

{#each options as [label, value], i}
    <RegisterRadio {label} bind:group={group} id={`input-${i}`} {value}/>
{/each}

<style>
</style>
