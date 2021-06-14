import Landing from "./routes/Landing.svelte";
import Login from "./routes/Login.svelte";
import RegisterStudent from "./routes/RegisterStudent.svelte";
import RegisterMaster from "./routes/RegisterMaster.svelte";
import Home from "./routes/Home.svelte";
import Search from "./routes/Search.svelte";
import Room from "./routes/Room.svelte";
import Teste from "./components/MasterMainInfo.svelte"

const routes = {
    "/": Landing,
    "/login": Login,
    "/register/student": RegisterStudent,
    "/register/master": RegisterMaster,
    "/home": Home,
    "/search": Search,
    "/room": Room,
    "/teste": Teste
}

export default routes;
