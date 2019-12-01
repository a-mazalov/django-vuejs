<template>
	<v-container fill-height class="login-page">
		<v-row align="center">
			<v-col md="6" sm="6" xs="12">
				<!-- <v-sheet class="text-left"> -->
				<div class="text-center">
					<!-- <h1 class="display-1">Хочешь научиться программировать?</h1> -->
					<h1 class="display-1">Продолжим учиться!</h1>
					<h3 class="font-weight-light">Получи доступ к десяткам бесплатных материалов</h3>
					<h3 class="font-weight-light">Общайся и учись у ведущих IT-специалистов</h3>
				</div>
				<!-- </v-sheet> -->
			</v-col>
			<v-col md="6" sm="6" xs="12">
				<!-- <form @submit.prevent="submit">
						<input v-model="inputs.username" type="text" id="username" placeholder="username" />
						<input v-model="inputs.password" type="password" id="password" placeholder="password" />
					</form>
				<button @click="login(inputs)" id="login-button">login</button>-->
				<h4 class="text-center headline my-4">Войти в аккаунт</h4>

				
				<v-card class="mx-auto pa-4" max-width="480" shaped :elevation="5">
					<v-alert v-if="login_fail" type="error">Ошибка авторизации. Неверный логин/пароль</v-alert>
					<v-card-text>
						<v-form ref="form" v-model="valid" class="pa-5">
							<v-text-field
								outlined
								v-model="inputs.username"
								type="text"
								id="username"
								label="Логин"
								prepend-inner-icon="fa-user"
								required
							></v-text-field>
							<v-text-field
								outlined
								v-model="inputs.password"
								id="password"
								label="Пароль"
								required
								prepend-inner-icon="fa-lock"
								:type="showPassword ? 'text' : 'password'"
								:append-icon="showPassword ? 'fa-eye' : 'fa-eye-slash'"
								@click:append="showPassword = !showPassword"
							></v-text-field>

							<div class="text-right">
								<v-breadcrumbs :items="urls" class="justify-end pa-0"></v-breadcrumbs>
							</div>

							<v-checkbox
								v-model="inputs.checkbox"
								label="Подтверждаю, что ознакомлен и принимаю условия"
								required
							></v-checkbox>
						</v-form>
					</v-card-text>
					<v-card-actions>
						<v-btn large block color="primary" @click="login(inputs)">Войти</v-btn>
					</v-card-actions>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
export default {
	data() {
		return {
			valid: true,
			showPassword: false,
			login_fail: false,
			inputs: {
				username: "",
				password: "",
				checkbox: false
			},
			urls: [
				{
					text: "Регистрация",
					to: "/register"
				},
				{
					text: "Забыл пароль?",
					to: "/password_reset"
				}
			]
		};
	},
	methods: {
		login({ username, password }) {
			this.login_fail = false;
			this.$store
				.dispatch("auth/login", { username, password })
				.then(() => this.$router.push("/"))
				.catch(()=> this.login_fail = true);
		}
	}
};
</script>

<style scoped>
#app {
	/* background: url('../assets/2720263.jpg') 50% 50%; */
	/* background: url('../assets/2043687.jpg') 50% 50%; */
	/* background-size: cover; */
}

.v-input__icon .v-icon.v-icon {
	font-size: 16px;
}
</style>
