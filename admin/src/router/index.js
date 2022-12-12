import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import Dishes from "@/views/Dishes.vue";
import CreateDish from "@/views/CreateDish";
import Orders from "@/views/Orders";
import Menu from "@/views/Menu";
import UserMenu from "@/views/UserMenu";
import AuthPage from "@/views/AuthPage";
import EditDay from "@/views/EditDay";


const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/auth",
        name: "Auth",
        component: AuthPage,
    },
    {
        path: "/dishes",
        name: "Dishes",
        component: Dishes,
    },
    {
        path: "/orders",
        name: "Orders",
        component: Orders,
    },
    {
        path: "/menu",
        name: "Menu",
        component: Menu,
    },
    {
        path: "/menu/:id",
        name: "MenuEdit",
        props:true,
        component: EditDay,
    },
    {
        path: "/dishes/create",
        name: "CreateDish",
        component: CreateDish,
    },
    {
        path: "/usermenu",
        name: "UserMenu",
        component: UserMenu,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;