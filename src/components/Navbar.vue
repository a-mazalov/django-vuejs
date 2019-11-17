<template>
	<v-app-bar app color="white" elevate-on-scroll
      scroll-target="#view">
		<v-app-bar-nav-icon></v-app-bar-nav-icon>

		<v-toolbar-title>Главная</v-toolbar-title>

		<v-spacer></v-spacer>

		<v-btn icon link to="/about">
			<v-icon>fa-address-card</v-icon>
		</v-btn>
		<v-btn icon link to="/logout">
			<v-icon>fa-sign-out-alt</v-icon>
		</v-btn>
	</v-app-bar>
</template>

<script>
	export default {
		name: "navbar"
	};
</script>

<style scoped>
</style>
