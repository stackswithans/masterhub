<script lang="typescript">
    import { reverse, postData, validateFormSection}  from "../scripts/utils";
    import { isLoggedIn, saveSessionData }  from "../scripts/auth";
    import { push }  from "svelte-spa-router";
    import MainLayout  from "../components/MainLayout.svelte";
    import Spinner  from "../components/Spinner.svelte";
    import LoginInput from "../components/login/LoginInput.svelte";

    if(isLoggedIn()) push("/search"); 

    let loading = false;

    let fields = {
        "email": null, 
        "password": null, 
    };

    let errors = {
        "email": [], 
        "password": [], 
    };

    const login = async () => {
        let hasErrors, result;
        loading = true;
        [hasErrors, result] = await validateFormSection("", "login", fields, errors, ["email", "password"]);
        if(hasErrors){
            errors = result;
            console.log(result);
            loading = false
            return;
        }
        loading = false;
        saveSessionData(result);
        push("/search");
    };

</script>


<Spinner loading={loading}/>
<MainLayout>
    <div class="login-layout">
        <aside class="image">
            <img src="/assets/images/login-img.png"  alt="A girl by the window">
        </aside>
        <aside class="form-container">
            <form>
                <h1 style="color:var(--color-4);"><span style="color:var(--color-2);">Master</span>Hub</h1>
                <div class="input-group">
                    <LoginInput errors={errors.email} bind:value={fields.email} name="email" description="E-mail"/>
                    <LoginInput errors={errors.password} bind:value={fields.password} name="password" type="password" description="Palavra-passe"/>
                </div>
                <button type="button" on:click={login}>Entrar</button>
            </form>
        </aside>
    </div>
</MainLayout>


<style>
    .login-layout{
        display: flex;
        font-size: 16px;
        width: 40.5em; /*width-height ratio: 0.6*/
        height: 24em;
        border: 1px solid transparent; 
        border-top-left-radius: 15px;
    }

    .image{
        display: flex;
        padding-top: 1rem;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        height: 100%;
        width: 50%;
        background-color: var(--color-4);
    }

    .image img{
        margin-top: 3em;
        max-width: 75%;
        max-height: 75%;
    }

    .form-container{
        flex-grow: 1;
        height: 100%;
        background-color: var(--color-3);
    }

    .form-container form{
        display: flex;
        width: 100%;
        height: 100%;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding-top: 3em;
    }

    .form-container .input-group{
        display: flex;
        width: 100%;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 0.8rem;
        margin: 2em 0 2em 0;
    }

    .form-container button{
        color: var(--color-4);
        background-color: var(--color-2);
        padding: 0.5rem 0 0.5rem 0;
        border: none;
        width: 75%;
    }

    .form-container button:hover{
        cursor: pointer;
        opacity: 0.8;
    }

    .form-container h1, 
    .form-container span{
        font-family:"Roboto Slab";
    }

    .form-container h1:hover{
        cursor: pointer;
    }

    @media(max-width: 1300px){
        .login-layout{
            font-size: 13px;
        }
    }

    @media(max-width: 1188px){
        .login-layout{
            font-size: 11px;
        }
    }
</style>
