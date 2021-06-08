<script lang="typescript">
    export let label = "";
    export let type: string = "text";
    export let name: string; 
    export let value = "";
</script>

<div>
    <label class="description">{label}</label>
    {#if type == "text"}
        <input name={name} bind:value={value} type="text" class="input-after">
    {:else}
        <input name={name} bind:value={value} type="password" class="input-after">
    {/if}
</div>

<style>
    .description{
        position: relative;
        font-family: "Roboto";
        font-weight: bold;
        font-size: 1rem;
        color: var(--color-3);
    }

    .input-after{
        width: 100%;
        margin-top: 1rem;
        border-radius: 5px;
    }

    .input-after:focus{
        outline: none;
    }
</style>
