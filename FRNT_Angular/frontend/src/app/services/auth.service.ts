import { Injectable } from "@angular/core";
import { environment } from "../../environments/environments";
import { HttpClient } from "@angular/common/http";
import { BehaviorSubject, Observable, tap } from "rxjs";


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
    private _isLoggedInSubject = new BehaviorSubject<boolean>(false);
    isLoggedIn$ = this._isLoggedInSubject.asObservable();

    constructor( private http: HttpClient) {}

    login(data: LoginData): Observable<any> {
        return this.http.post(`${this.base}/login`, data).pipe(tap(() => this._isLoggedInSubject.next(true)));
    }

    register(data: RegisterData): Observable<any> {
        return this.http.post(`${this.base}/register`, data);
    }

    logout(){
        this._isLoggedInSubject.next(false);
    }
}