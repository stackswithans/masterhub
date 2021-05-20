
<script lang="typescript">
    export let video: HTMLVideoElement;
    export let caption: string; 
</script>


<div>
    <video bind:this={video}></video>
    <p class="caller-name">{caption}</p>
</div>

<style>
    div {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        box-sizing: border-box;
        border-radius: 35px;
        max-width:60%;
        height:60%;
    }

    video{
        display: flex;
        border:1px solid transparent;
        width: 100%;
        height: 100%;
    }

    .caller-name{
        text-align: center;
        margin-top: 1rem;
        width: fit-content;
        border-radius: 15px;
        font-size: 1rem;
        box-sizing: border-box;
        padding: 0.5rem;
    }
</style>
