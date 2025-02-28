<template>
    <div id="register__background">
        <img class="background__shape1" src="@/assets/svg/Vector.svg" alt="Vector">
        <img class="background__shape2" src="@/assets/svg/backgroundShape.svg" alt="backgroundSape">
    </div>
    <div class="register__container">
        <h1 class="register__container--header"> Register</h1>
        <div class="form__container">
            <input class="register__input" type="text" placeholder="Full name" aria-label="Full name">
            <input class="register__input" type="email" placeholder="Email" aria-label="Email">
            <input class="register__input" type="password" placeholder="Password" aria-label="Password">
            <input class="register__input" type="password" placeholder="Confirm Password"
                aria-label="Confirm password">
            <input class="register__input" type="date" placeholder="Birthday" aria-label="Birthday">
            <select id="States" name="states" class="register_input">
            <option value="" selected disabled>State</option>
            <option value="aguascalientes">Aguascalientes</option>
            <option value="baja_california">Baja California</option>
            <option value="baja_california_sur">Baja California Sur</option>
            <option value="campeche">Campeche</option>
            <option value="coahuila">Coahuila</option>
            <option value="colima">Colima</option>
            <option value="chiapas">Chiapas</option>
            <option value="chihuahua">Chihuahua</option>
            <option value="cdmx">Ciudad de México</option>
            <option value="durango">Durango</option>
            <option value="guanajuato">Guanajuato</option>
            <option value="guerrero">Guerrero</option>
            <option value="hidalgo">Hidalgo</option>
            <option value="jalisco">Jalisco</option>
            <option value="mexico">México</option>
            <option value="michoacan">Michoacán</option>
            <option value="morelos">Morelos</option>
            <option value="nayarit">Nayarit</option>
            <option value="nuevo_leon">Nuevo León</option>
            <option value="oaxaca">Oaxaca</option>
            <option value="puebla">Puebla</option>
            <option value="queretaro">Querétaro</option>
            <option value="quintana_roo">Quintana Roo</option>
            <option value="san_luis_potosi">San Luis Potosí</option>
            <option value="sinaloa">Sinaloa</option>
            <option value="sonora">Sonora</option>
            <option value="tabasco">Tabasco</option>
            <option value="tamaulipas">Tamaulipas</option>
            <option value="tlaxcala">Tlaxcala</option>
            <option value="veracruz">Veracruz</option>
            <option value="yucatan">Yucatán</option>
            <option value="zacatecas">Zacatecas</option>
        </select>

        <div class="create__account--container">
            <button class="create--account">
                Create account
            </button>
        </div>


        </div>

       
        <p class="register__text">
            By clicking "Create account" you agree to our<button class="terms__button">terms</button> and <button
                class="privacy__button"> privacy policy</button>.
        </p>
    </div>
</template>

<style scoped>
@import "@/assets/styles/RegisterComponent.css"
</style>