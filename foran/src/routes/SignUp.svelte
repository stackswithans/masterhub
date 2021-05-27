<script lang="typescript">
    import NavBar from "../components/NavBar.svelte";
    import RegisterForm  from "../components/RegisterForm.svelte";

    let step = 1;
</script>

<div class="container">
    <NavBar theme="light"/>
    <main class="content">
        <div class="form-layout">
            <aside class="image">
                <p>Seja bem-vindo, caro estudante!</p>
                <img src="/assets/images/register-img-1.png" alt="">
            </aside>
            <RegisterForm/>
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

    .form-layout .image{
        display: flex;
        padding-top: 1rem;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        width: 36%;
        height: 100%;
        background-color: var(--color-3);
    }

    .form-layout .image p{
        color: white;
        font-family: "Roboto Condensed";
        font-size: 1.4em; 
    }

    .form-layout .image img{
        margin-top: 3em;
        max-width: 90%;
        max-height: 90%;
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
