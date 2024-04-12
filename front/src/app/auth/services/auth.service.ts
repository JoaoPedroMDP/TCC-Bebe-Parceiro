import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Observable, catchError, tap, throwError } from 'rxjs';
import { APP_CONFIG, Benefited, UserToken } from 'src/app/shared';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
 

  private baseURL!: string;

  constructor(private http: HttpClient, private cookieService: CookieService) {
    this.baseURL = APP_CONFIG.baseURL;
  }

  /**
   * @description Faz um GET para obter todas as cidades cadastradas no sistema
   * @param stateId o Id do Estado/Província selecionado para filtrar as cidades
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getCities(stateId: number): Observable<any> {
    return this.http.get(`${this.baseURL}cities?state_id=${stateId}`, { headers: this.getHeaders() });
  }

  /**
   * @description Faz um GET para obter todos os Países cadastrados no sistema
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getCountries(): Observable<any> {
    return this.http.get(`${this.baseURL}countries`, { headers: this.getHeaders() });
  }

  /**
   * @description Dado que os Services em Angular são um singleton, então uma única instância
   * será utilizada mesmo variando entre componentes, e pelo fato dos headers terem valores
   * varíaveis como o token de authenticação nós precisamos alterar a depender do método,
   * Eu havia pensado em utilizar um atributo e passar o valor no construtor, mas não
   * estava sendo possível atualizar o valor como explicado acima, utilizando esse método
   * a cada chamada de algum método do service terá o seus valores de headers atualizados
   * @returns Os Headers para serem utilizados na chamada rest
   */
  getHeaders(): HttpHeaders {
    const userToken = this.getUser(); // Retorna o UserToken atualizado
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Token ${userToken?.token}`
    });
  }

  /**
   * @description Faz um GET para obter todos os Estados Civis cadastrados no sistema
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getMaritalStatuses(): Observable<any> {
    return this.http.get(`${this.baseURL}marital_statuses`, { headers: this.getHeaders() });
  }

  /**
   * @description Faz um GET para obter todos os Programas Sociais cadastrados no sistema
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getSocialPrograms(): Observable<any> {
    return this.http.get(`${this.baseURL}social_programs`, { headers: this.getHeaders() });
  }

  /**
   * @description Faz um GET para obter todos os Estados/Províncias cadastrados no sistema
   * @param countryId o Id do Pais selecionado para filtrar os estados
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getStates(countryId: number): Observable<any> {
    return this.http.get(`${this.baseURL}states?country_id=${countryId}`, { headers: this.getHeaders() });
  }

  /**
   * @description Obtém um usuário através de um cookie salvo no navegador
   * @returns Objeto do tipo `UserToken` contendo o token, dados e expiração
   */
  getUser(): UserToken {
    const userToken = this.cookieService.get('user');
    return userToken ? JSON.parse(userToken) : null;
  }

  /**
   * @description Realiza um POST para fazer a autenticação do usuário
   * @param value um objeto { username: string, password: string } para fazer a autenticação
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  login(value: { username: string, password: string }): Observable<any> {
    return this.http.post(`${this.baseURL}auth/login`, value, { headers: this.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(error.status));
        })
      );
  }

  /**
   * @description Realiza um POST para fazer o logout do usuário e apagar os cookies
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  logout(): Observable<any> {
    // O Método post do HttpClient não aceita a chamada de um post sem o argumento do
    // body, então é necessário incluir o um objeto vazio '{}' no segundo argumento, 
    // caso contrário será retornado erro
    return this.http.post(`${this.baseURL}auth/logout`, {}, { headers: this.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(error.status));
        }),
        tap(() => {
          // Apaga o token no frontend
          this.cookieService.delete('user', '/');
        })
      );
  }

  /**
   * @description Faz um POST para inserir os dados de beneficiada
   * @param benefited O objeto beneficiada para ser enviado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  saveBenefited(benefited: Benefited): Observable<any> {
    return this.http.post(`${this.baseURL}beneficiaries`, benefited, { headers: this.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para validar o código e prosseguir com o cadastro de beneficiada
   * @param code O código de acesso como parametro na URL
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  sendCode(code: string): Observable<any> {
    return this.http.get(`${this.baseURL}access_codes/check?code=${code}&used=false`,
      {
        observe: 'response', headers: this.getHeaders()
      });
  }

  /**
   * @description Armazena um cookie do usuário no navegador
   * @param user Objeto do tipo `UserToken` contendo o token, dados e expiração
   */
  setUser(user: UserToken) {
    this.cookieService.set('user', JSON.stringify(user), 1, '/');
  }

  

}
