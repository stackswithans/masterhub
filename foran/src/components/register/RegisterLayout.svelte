<script lang="typescript">
    import NavBar from "../NavBar.svelte";
</script>

<div class="container">
    <NavBar brand={true} theme="light"/>
    <main class="content">
        <div class="form-layout">
            <slot></slot>
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
        font-size: 16px;
        width: 55.5em; /*width-height ratio: 0.49*/
        height: 27.195em;
    }

    @media(max-width: 1300px){
        .form-layout{
            font-size: 13px;
        }
    }

    @media(max-width: 1188px){
        .form-layout{
            font-size: 11px;
        }
    }
</style>
