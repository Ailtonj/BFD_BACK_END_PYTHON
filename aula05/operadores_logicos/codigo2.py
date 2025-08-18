valor_da_compra = 120
esta_usando_cupom = False
e_membro_premium = False

tem_direito_a_frete_gratis = (valor_da_compra > 100 and not esta_usando_cupom) or e_membro_premium

print(f"O cliente tem direito a frete gratis? {tem_direito_a_frete_gratis}")