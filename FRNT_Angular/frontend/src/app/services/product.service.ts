import { Injectable } from "@angular/core";
import { environment } from "../../environments/environments";
import { HttpClient, HttpParams } from "@angular/common/http";
import { Observable } from "rxjs";


export interface Product {
Price: string|number;
imageBack: any;
inStock: any;
price: string|number;
imageFront: any;
    id: number;
    name: string;
    description: string;
}

@Injectable({
    providedIn: "root",
})
export class ProductService {
    private base = `${environment.apiUrl}/products`; // API URL do environment

    constructor(private http: HttpClient) {}

    getAll(): Observable<Product[]> {
        return this.http.get<Product[]>(this.base);
    }

    getByName(name: string): Observable<Product[]> {
        const params = new HttpParams().set("name", name);
        return this.http.get<Product[]>(this.base, { params });
}
}
