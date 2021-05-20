
<script lang="typescript">
    export let video: HTMLVideoElement
</script>

<video bind:this={video}></video>

<style>
    video{
        display: flex;
        border-radius: 15px;
        background: red;
        max-width: 60%;
        max-height: 60%;
    }
</style>
