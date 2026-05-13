import streamlit as st
import sympy as sp

def main():
    st.set_page_config(page_title="Calculadora de Derivadas", page_icon="🧮")
    
    st.title("🧮 Calculadora de Derivadas Pro")
    st.markdown("Introduce una función de $x$ y el orden de la derivada que deseas obtener.")

    # --- BARRA LATERAL (Configuración) ---
    st.sidebar.header("Configuración")
    orden = st.sidebar.number_input("Orden de la derivada", min_value=1, max_value=10, value=1)
    simplificar = st.sidebar.checkbox("Simplificar resultado", value=True)

    # --- CUERPO PRINCIPAL ---
    expr_usuario = st.text_input("Función f(x):", placeholder="Ejemplo: 3*x**2 + sin(x)")

    if expr_usuario:
        try:
            # Definir símbolo y procesar función
            x = sp.Symbol('x')
            expr_limpia = expr_usuario.replace('ln', 'log')
            funcion = sp.sympify(expr_limpia)
            
            # Cálculo
            derivada = sp.diff(funcion, x, orden)
            if simplificar:
                derivada = sp.simplify(derivada)

            # --- RESULTADOS ---
            st.divider()
            st.subheader("Resultados")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.info("**Entrada:**")
                st.latex(sp.latex(funcion))
            
            with col2:
                st.success(f"**Derivada (Orden {orden}):**")
                st.latex(sp.latex(derivada))

            # Código para copiar
            st.text_area("Formato Python (Raw):", str(derivada), help="Copia este texto para usarlo en tu código.")

        except Exception as e:
            st.error(f"Hubo un error al procesar la función. Asegúrate de usar la sintaxis correcta.")
            st.exception(e)

if __name__ == "__main__":
    main()