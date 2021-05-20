
<script lang="typescript">
    export let text: string;
    export let className: string = "";
</script>

<button class="{className}" on:click>{text}</button>

<style>
    button{
        padding: 0.5rem;
        color: white;
        border: None;
        background-color: #4A5955;
        width: fit-content;
    }

    button:hover{
        cursor: pointer;
    }
</style>
