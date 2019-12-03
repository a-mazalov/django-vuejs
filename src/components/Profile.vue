<template>
	<v-container style="margin-top: 60px;" fill-height>
		<v-container class="mb-0" fill-height>
			<v-row justify="center" align="center" no-gutters>
				<v-col class="d-flex justify-center">
					<v-img src="../assets/banner_img.png" max-width="700" contain></v-img>
				</v-col>
				<v-col>
					<div>
						<h1 class="display-3 text-center">Мой профиль</h1>
					</div>
					<!-- {{userInfo}} -->
					<v-card outlined class="mt-10 pa-5">
						<!-- <v-card-text> -->
						<v-list two-line>
							<v-list-item>
								<v-list-item-icon>
									<v-icon color="indigo">mdi-shield-account</v-icon>
								</v-list-item-icon>

								<v-list-item-content>
									<v-list-item-subtitle>Username</v-list-item-subtitle>
									<v-list-item-title>{{ userInfo.username }}</v-list-item-title>
								</v-list-item-content>

								<!-- <v-list-item-icon>
									<v-icon>mdi-message-text</v-icon>
								</v-list-item-icon>-->
							</v-list-item>

							<v-list-item>
								<v-list-item-action></v-list-item-action>

								<v-list-item-content>
									<v-list-item-subtitle>ФИО</v-list-item-subtitle>
									<v-list-item-title>{{ userInfo.first_name }} {{ userInfo.last_name }}</v-list-item-title>
								</v-list-item-content>

								<!-- <v-list-item-icon>
									<v-icon>mdi-message-text</v-icon>
								</v-list-item-icon>-->
							</v-list-item>

							<v-divider inset></v-divider>

							<v-list-item>
								<v-list-item-icon>
									<v-icon color="indigo">mdi-email</v-icon>
								</v-list-item-icon>

								<v-list-item-content>
									<v-list-item-title>{{ userInfo.email }}</v-list-item-title>
									<v-list-item-subtitle>Почта</v-list-item-subtitle>
								</v-list-item-content>
							</v-list-item>

							<v-list-item>
								<v-list-item-action></v-list-item-action>

								<v-list-item-content>
									<v-list-item-subtitle>Последняя авторизация</v-list-item-subtitle>
									<v-list-item-title>{{ $moment(userInfo.last_login).format('DD-MM-YYYY HH:MM')  }}</v-list-item-title>
								</v-list-item-content>

								<v-list-item-content>
									<v-list-item-subtitle>Зарегистрирован</v-list-item-subtitle>
									<v-list-item-title>{{ $moment(userInfo.date_joined).format('DD-MM-YYYY') }}</v-list-item-title>
								</v-list-item-content>

							</v-list-item>

							<v-divider inset></v-divider>

							<v-list-item>
								<v-list-item-icon>
									<!-- <v-icon color="indigo">mdi-map-marker</v-icon> -->
								</v-list-item-icon>

								<v-list-item-content>
									<v-list-item-title>
										<strong>Участвую в курсах:</strong>
									</v-list-item-title>
									<!-- <v-list-item-subtitle>Orlando, FL 79938</v-list-item-subtitle> -->
								</v-list-item-content>
							</v-list-item>

							<div v-for="course in userInfo.courses" :key="course.id">
								<v-divider inset></v-divider>
								<v-list-item :to="`/courses/${course.id}`">
									<v-list-item-icon>
										<v-icon color="indigo">mdi-menu-right</v-icon>
									</v-list-item-icon>

									<v-list-item-content>
										<v-list-item-title>{{ course.name }} ({{ course.level }})</v-list-item-title>
										<v-list-item-subtitle>{{ course.date_start }}</v-list-item-subtitle>
									</v-list-item-content>

									<v-list-item-icon>
										<v-icon>
											mdi-open-in-new
										</v-icon>
									</v-list-item-icon>
								</v-list-item>
							</div>
						</v-list>
					</v-card>

					<!-- <v-divider width="350px"></v-divider> -->
				</v-col>

				<!-- <v-col cols="12"> -->
				<!-- </v-col> -->
			</v-row>
		</v-container>
	</v-container>
</template>

<script>
	import { mapState, mapActions, mapGetters } from "vuex";
	import auth from "../api/auth";

	export default {
		name: "About",
		data() {
			return {
				subject: "",
				msgBody: "",
				user: null
			};
		},
		computed: {
			...mapState({
				course: function(state) {
					return state.courses.courses.find(obj => obj.id == 1);
				}
			}),
			...mapGetters("auth", ["userInfo"])
		},
		methods: {
			...mapActions("courses", ["addCourse", "deleteCourse"]),

			followCourse(crsId) {
				this.$store.dispatch("courses/joinCourse", crsId);
			},
			unFollowCourse(crsId) {
				this.$store.dispatch("courses/outCourse", crsId);
			},

			coloredIcons(language) {
				let color = "grey";

				switch (language) {
					case "javascript":
						color = "orange";
						break;
					case "python":
						color = "primary";
						break;
					case "php":
						color = "deep-purple lighten-1";
						break;
				}

				return color;
			}
		},

		created() {
			// this.course = courses.filter(obj => obj.id == this.$route.params)

			// auth.getAccountDetails().then(response =>
			// 	this.user = response.data
			// )

			this.$store.dispatch("auth/userInfo");
			this.$store.dispatch("courses/getCourses");
			// console.log(
			// 	this.$store.state.courses.courses.filter(
			// 		obj => obj.id == this.$route.params.id
			// 	)
			// );
		}
	};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	hr {
		max-width: 65%;
	}

	.msg {
		margin: 0 auto;
		max-width: 30%;
		text-align: left;
		border-bottom: 1px solid #ccc;
		padding: 1rem;
	}

	.msg-index {
		color: #ccc;
		font-size: 0.8rem;
		/* margin-bottom: 0; */
	}

	img {
		width: 250px;
		padding-top: 50px;
		padding-bottom: 50px;
	}
</style>
