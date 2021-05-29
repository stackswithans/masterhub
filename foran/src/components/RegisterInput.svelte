<script lang="typescript">
    export let label = "";
    export let type: string = "text";
</script>

<div>
    <label class="description">{label}</label>
    <input type="{type}" class="input-after">
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
