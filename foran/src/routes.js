import Landing from "./routes/Landing.svelte";
import Login from "./routes/Login.svelte";
import RegisterStudent from "./routes/RegisterStudent.svelte";
import RegisterMaster from "./routes/RegisterMaster.svelte";
import Home from "./routes/Home.svelte";
import Search from "./routes/Search.svelte";
import Teste from "./components/MasterInList.svelte";

const routes = {
    "/": Landing,
    "/login": Login,
    "/register/student": RegisterStudent,
    "/register/master": RegisterMaster,
    "/home": Home,
    "/search": Search,
    "/teste": Teste
}

export default routes;
