<script lang="typescript">
    export let value: string;
</script>

<input bind:value={value} type="text"  id="join-input"/>

<style>
    input{
        color: white;
        border: None;
        background: transparent;
        border-bottom: 3px solid #4A5955;
    }

    input:focus{
        outline: None;
    }
</style>
