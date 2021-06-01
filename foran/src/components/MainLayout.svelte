<script lang="typescript">
    import NavBar from "./NavBar.svelte";
</script>

<div class="container">
    <div class="overlay"></div>
    <img class="background" src="/assets/images/main_bg.png" alt="A library"/>
    <NavBar brand={true} theme="light"/>
    <main class="content">
        <slot></slot>
    </main>
</div>


<style>
    .container{
        position: relative;
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100vh;
    }

    .overlay, .background{
        position: fixed;
        width: 100%;
        height: 100%;
    }

    .overlay{
        z-index: -1;
        opacity: 0.5;
        background-color: var(--color-2);
    }

    .background{
        z-index: -2;
    }

    .content{
        display: flex;
        flex-grow: 1;
        justify-content: center;
        align-items: center;
    }
</style>
