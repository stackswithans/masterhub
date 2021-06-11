<script lang="typescript">
    export let loading = false;
    let visible = false;
    $:{
        if(loading){
            visible = true;
        }
        else{
            setTimeout(() => {
                visible = false;
            }, 500)
        }
    }

</script>

{#if visible}
    <div class="overlay">
        <div class="loader"></div>
    </div>
{/if}



<style>
    .overlay{
        display: flex;
        align-items: center;
        justify-content: center;
        position: fixed;
        height: 100vh;
        width: 100vw;
        z-index: 100;
        background-color: black;
        opacity: 0.9;
    }

    .loader {
      border: 0.5rem solid var(--color-3); /* Light grey */
      border-top: 0.5rem solid var(--color-2); /* Blue */
      border-radius: 50%;
      width: 120px;
      height: 120px;
      animation: spin 2s linear infinite;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
</style>
