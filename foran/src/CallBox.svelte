
<script lang="typescript">
    export let stream: MediaStream;
    $: document.querySelector("video").srcObject = stream;
</script>

<video></video>

<style>
    video{


    }
</style>
