<script lang="typescript">
    export let description: string = "";
</script>

<input type="text" placeholder={description} class="input-after">

<style>
    .input-after{
        width: 18rem;
        border-radius: 5px;
        text-indent: 1rem;
    }

    .input-after::placeholder{
        color: var(--color-6);
        font-size: 1.2rem;
        font-family: "Roboto Condensed";
    }

    .input-after:focus{
        outline: none;
    }

</style>
