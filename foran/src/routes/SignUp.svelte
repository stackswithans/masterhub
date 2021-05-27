<script lang="typescript">
    import NavBar from "../components/NavBar.svelte";
</script>

<div class="container">
    <NavBar theme="light"/>
    <main class="content">
        <div class="form-layout">
            <aside class="image"></aside>
            <aside class="form"></aside>
        </div>
    </main>
</div>


<style>
    .container{
        position: relative;
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100vh;
        background-color: #141414;
    }

    .content{
        display: flex;
        flex-grow: 1;
        justify-content: center;
        align-items: center;
    }


    .form-layout{
        display: flex;
        width: 78%;
        height: 68%;
    }

    .form-layout .image{
        width: 40%;
        height: 100%;
        background-color: var(--color-3);
    }

    .form-layout .form{
        flex-grow: 1;
        height: 100%;
        background-color: var(--color-4);
    }
</style>
