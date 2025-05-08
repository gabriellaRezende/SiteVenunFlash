import { Injectable } from "@angular/core";
import { environment } from "../../environments/environments";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";


interface LoginData {
    username: string;
    password: string;
}
interface RegisterData {
    username: string;
    password: string;
    email: string;
    Name: string;
    phone?: string;
}

@Injectable({
    providedIn: "root",})
export class AuthService {
    private base = `${environment.apiUrl}`; // API URL do environment

    constructor( private http: HttpClient) {}

    login(data: LoginData): Observable<any> {
        return this.http.post(`${this.base}/login`, data);
    }

    register(data: RegisterData): Observable<any> {
        return this.http.post(`${this.base}/register`, data);
    }
}