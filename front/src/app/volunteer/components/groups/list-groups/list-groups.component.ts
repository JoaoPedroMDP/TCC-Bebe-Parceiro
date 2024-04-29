import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Group } from 'src/app/shared';
import { GroupService } from 'src/app/volunteer/services/group.service';


@Component({
  selector: 'app-list-groups',
  templateUrl: './list-groups.component.html',
  styleUrls: ['./list-groups.component.css']
})
export class ListGroupsComponent implements OnInit, OnDestroy {

  @Input() groups!: Group[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private groupService: GroupService, private modalService: NgbModal) { }

  ngOnInit(): void {
    this.listGroups(false); // Inicialmente lista as funções.
    // Se inscreve no Observable de atualização. Quando um novo valor é emitido, chama a listagem novamente.
    this.subscription = this.groupService.refreshPage$.subscribe(() => {
      this.listGroups(false); // Lista as funções novamente para refletir as atualizações.
    })
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe(); // Cancela a subscrição para evitar vazamentos de memória.
  }

  /**
   * @description Lista todas as funções no componente
   * @param isFiltering boolean que indica se a listagem será filtrada ou não
   */
  listGroups(isFiltering: boolean){
    this.isLoading = true; // Flag de carregamento
    this.groupService.listGroups().subscribe({
      next: (response) => {
        this.groups = response
        // Ordena por nome crescente
        this.groups.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e),
      complete: () => { 
        if (isFiltering) {
          this.groups = this.groups.filter(
            (group: Group) => {
              // Asegura que name é uma string antes de chamar métodos de string
              return group.name ? group.name.toLowerCase().includes(this.filter.toLowerCase()) : false;
            }
          );
        }
        this.isLoading = false;
      }
    })
  }

  
  /**
   * @description Verifica se o usuário está filtrando dados e chama os métodos
   * @param event Um evento do input
   */
  filterGroup(event: Event) {
    if (event != undefined) {
      this.groups = []; // Esvazia o array

      // A ideia tem que ser se tiver string então filtrar 
      if (this.filter != '') {
        this.listGroups(true)
      } else {
        // se não tiver então a gente filtra tudo
        this.listGroups(false);
      }
    }
  }

 
}
