
<script lang="typescript">
    import RegisterRadio from "../components/RegisterRadio.svelte";
    export let options: Array<[string, string, boolean?]>;
    export let group: string;

    options = options.map(([label, value, checked]) => {
        return (checked === undefined) ? [label, value, false] : [label, value, checked];
    });
</script>

{#each options as [label, value, checked], i}
    <RegisterRadio {label} bind:group={group} id={`input-${i}`} checked={checked} {value}/>
{/each}

<style>
</style>
