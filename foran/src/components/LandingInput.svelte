<script lang="typescript">
    export let label: string;
    export let large: boolean = false;
</script>

<div>
    <label for="">{label}</label>
    {#if large}
        <textarea id="" name="" cols="30" rows="10"></textarea>
    {:else}
        <input type="text"/>
    {/if}
</div>



<style>
    label{
        font-size: 1rem;
        font-family:"Roboto";
        color: var(--color-6);
    }

    textarea{ resize: none; }

    input, textarea{
        background: None;
        border: none;
        border-bottom: 1px solid var(--color-6);
        font-family:"Roboto";
        color: var(--color-3);
    }

    input:focus, textarea:focus{
        outline: None;
        border-bottom: 1px solid var(--color-3);
    }
</style>
