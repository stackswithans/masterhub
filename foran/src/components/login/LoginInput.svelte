<script lang="typescript">
    export let name: string;
    export let value: string;
    export let type: string = "text";
    export let description: string = "";
</script>

{#if type === "text"}
    <input {name} bind:value={value} type="text" placeholder={description} class="input-after">
{:else}
    <input {name} bind:value={value} type="password" placeholder={description} class="input-after">
{/if}

<style>
    .input-after{
        width: 75%;
        border-radius: 5px;
        text-indent: 1rem;
    }

    .input-after::placeholder{
        color: var(--color-6);
        font-size: 1rem;
        font-family: "Roboto Condensed";
    }

    .input-after:focus{
        outline: none;
    }

</style>
