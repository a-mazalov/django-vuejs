<template>
	<v-app id="app">
		<navbar v-if="isAuthenticated"></navbar>
		<router-view />
	</v-app>
</template>

<script>
import { mapGetters } from "vuex";

import Navbar from "./components/Navbar";

export default {
	name: "app",
	components: {
		Navbar
	},
	computed: mapGetters("auth", ["isAuthenticated"])
};
</script>

<style>

</style>
