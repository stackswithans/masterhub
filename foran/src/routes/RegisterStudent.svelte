<script lang="typescript">
    import RegisterAside  from "../components/RegisterAside.svelte";
    import RegisterForm  from "../components/RegisterForm.svelte";
    import RegisterLayout  from "../components/RegisterLayout.svelte";
</script>


<RegisterLayout>
    <RegisterAside header="Seja bem-vindo, caro estudante!" src="/assets/images/register-img-1.png" alt="Girl studying"/>
    <RegisterForm/>
</RegisterLayout>
